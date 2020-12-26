import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs/internal/BehaviorSubject';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { CountryGame } from '../models/country_game';
import { GAME_COUNTRIES_QUANTITY, LIVES_QUANTITY, POINTS_LOSE_BATTLE, POINTS_WIN_BATTLE, POINTS_WORLD_DOMINATION } from '../services/rules';

@Injectable({
  providedIn: 'root'
})
export class GameStatusService {
  readonly ROOT_URL = 'http://localhost:8000'
  
  conquered_order = [];
  country = new BehaviorSubject<string>('');
  username = new BehaviorSubject<string>('');
  points = new BehaviorSubject<number>(0);
  conquered = new BehaviorSubject<number>(1);
  max_conquered = new BehaviorSubject<number>(1);
  isStarted = new BehaviorSubject<boolean>(false);
  isCountryPicked = new BehaviorSubject<boolean>(false);
  inBattle = new BehaviorSubject<boolean>(false);
  lives = new BehaviorSubject<number>(LIVES_QUANTITY);
  countries = new BehaviorSubject<CountryGame[]>([]);
  gameEnded = new BehaviorSubject<boolean>(false);
  winOrLose = new BehaviorSubject<boolean>(false);
  changeFact = new BehaviorSubject<boolean>(true);
  revealAnswer = new BehaviorSubject<boolean>(true);
  hint = new BehaviorSubject<boolean>(true);



  countryModified = this.country.asObservable();
  usernameModified = this.username.asObservable();
  pointsModified = this.points.asObservable();
  conqueredMoified = this.conquered.asObservable();
  startedModified = this.isStarted.asObservable();
  countryPicked = this.isCountryPicked.asObservable();
  battleStatus = this.inBattle.asObservable();
  livesModified = this.lives.asObservable();
  gameEndedModified = this.gameEnded.asObservable();
  winOrLoseModified = this.winOrLose.asObservable();
  maxConqueredModified = this.max_conquered.asObservable();
  hintModified = this.hint.asObservable();
  revealModified = this.revealAnswer.asObservable();
  changeFactModified = this.changeFact.asObservable();
  countriesModified: any;
  
  constructor(private http: HttpClient) {
  }

  /* Start new game */
  startGame() {
    this.isStarted.next(true);
    this.points.next(0);
    this.lives.next(LIVES_QUANTITY);
    this.conquered.next(1);
    this.max_conquered.next(1);
    this.inBattle.next(false);
    this.winOrLose.next(false);
    this.gameEnded.next(false);
    this.isCountryPicked.next(false);
  }

  /* Inform Game status that the game have finished */
  endGame() {
    this.isStarted.next(false);
  }

  /* Inform the user selected a country to compete with */
  selectCountry(country: string) {
    this.country.next(country);
    this.isCountryPicked.next(true);
  }

  /* Inform the user retracted and disselect his country  */
  disselectCountry() {
    this.country.next('');
    this.isCountryPicked.next(false);
  }

  /* Inform the user defeated a country and take control over his area */
  defeatCountry(points: number) {
    this.points.next(this.points.getValue() + points);
    this.conquered.next(this.conquered.getValue() + 1);
    this.inBattle.next(false);
  }

  /* Inform the user is in state of battle against certain country */
  battleState() {
    this.inBattle.next(true);
  }

  /* Inform the user ended his battle */
  endBattleState() {
    this.inBattle.next(false);
  }

  /* Inform the user use helper option */
  useHint() {
    this.hint.next(false);
  }
  useChangeFact() {
    this.changeFact.next(false);
  }
  useRevealAnswer() {
    this.revealAnswer.next(false);
  }
  
  wonBattle(rival_country: CountryGame) {
      /* update status and map */
      this.inBattle.next(false);
      var countries = this.countries.getValue();
      countries[rival_country.id].name = this.country.getValue();
      countries[rival_country.id].isConquered = true;
      this.countries.next(countries);
      this.conquered_order.push(rival_country);

      /* gain acheivements  */
      this.increase_points(POINTS_WIN_BATTLE);
      this.conquered.next(this.conquered.getValue() + 1);
      this.max_conquered.next(Math.max(this.max_conquered.getValue(), this.conquered.getValue()));

      /* check if the game is over */
      if (this.conquered.getValue() == GAME_COUNTRIES_QUANTITY)
          this.worldDomination();
  }

  /* The user dominate the entire world and won the game */
  worldDomination() {
      this.increase_points(POINTS_WORLD_DOMINATION);
      this.gameEnded.next(true);
      this.winOrLose.next(true);
      /* update scores data table */
  }

  is_live_descrease() {
      return this.conquered.getValue() == 1 && this.lives.getValue() > 1;
  }

  /* lost in battle */
  lost_battle(rival_country: CountryGame) {
      this.inBattle.next(false);
      if (this.conquered.getValue() == 1 && this.lives.getValue() > 1) {
          this.lives.next(this.lives.getValue() - 1);
          return;
      }
      let latest_conquered = this.conquered_order.pop();
      var countries = this.countries.getValue();
      countries[latest_conquered.id].name = rival_country.name;
      countries[latest_conquered.id].isConquered = false;
      this.countries.next(countries);
      this.increase_points(POINTS_LOSE_BATTLE);
      this.conquered.next(this.conquered.getValue() - 1);

      if (this.conquered.getValue() == 0)
          this.game_over();
    }
  
  game_over() {
      this.gameEnded.next(true);
      this.winOrLose.next(false);
  }

  /* add additional points */
  increase_points(points: number) {
      var total_points = Math.max(this.points.getValue() + points, 0);
      this.points.next(total_points);
  }

  /* Select randomly the countries that take part in the game and competing against the user */
  select_rival_countries(): Observable<String[]>  {
    this.countriesModified = this.http.get<String[]>(this.ROOT_URL + '/countries/game');
    this.countriesModified.subscribe(countries => {
        var countriesArray = [];
        if (countries == null)
          return;
        for (var i = 0; i < countries.length; i++) {
            var cur_country = new CountryGame();
            cur_country.id = i;
            cur_country.name = (i == 2) ? this.country.getValue() : countries[i];
            cur_country.isConquered = (i == 2) ? true : false;
            countriesArray.push(cur_country);
        }
        this.conquered_order.push(countriesArray[2]);
        this.countries.next(countriesArray);
    })
    return this.countriesModified;
  }

}
