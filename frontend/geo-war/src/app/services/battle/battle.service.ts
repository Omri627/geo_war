import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { Fact } from '../../models/fact';
import { HttpClient } from '@angular/common/http';
import { GameStatusService } from 'src/app/game/status.service';
import { FACTS_QUANTITY, POINTS_CORRECT_ANSWER, POINTS_WIN_BATTLE } from '../rules';
import { CountryGame } from 'src/app/models/country_game';

@Injectable({
  providedIn: 'root'
})
export class BattleService {
  readonly ROOT_URL = 'http://localhost:8000'

  user_country = new BehaviorSubject<string>('');
  rival_country = new BehaviorSubject<CountryGame>(null);
  facts = new BehaviorSubject<Fact[]>(null);
  current_fact = new BehaviorSubject<number>(0);
  corrent = new BehaviorSubject<number>(0);
  is_end = new BehaviorSubject<boolean>(false);
  win_or_lost = new BehaviorSubject<boolean>(false);

  constructor(private http: HttpClient, private status: GameStatusService) {
  }

  startBattle(user_country: string, rival_country: CountryGame) {
      this.user_country.next(user_country);
      this.rival_country.next(rival_country);
      this.is_end.next(false);
      this.current_fact.next(0);
      this.corrent.next(0);
      this.buildFacts();
  }

  buildFacts() {
      var facts_response = this.http.get<Fact[]>(this.ROOT_URL + '/facts/' + this.user_country.getValue() + '/vs/' + this.rival_country.getValue().name);
      facts_response.subscribe(facts_set => this.facts.next(facts_set));
  }

  getCurrentFact() {
      console.log(this.facts.getValue());
      var current_id = this.current_fact.getValue();
      var current_fact = this.facts.getValue()[current_id];
      return current_fact;
  }

  assignAnswer(answer: boolean) {
      var current_fact = this.getCurrentFact();
      if (current_fact.answer == answer) {
          this.status.increase_points(POINTS_CORRECT_ANSWER);
          this.corrent.next(this.corrent.getValue() + 1);
      }
      this.nextFact();        
  }

  nextFact() {
    var fact_number = this.current_fact.getValue() + 1;
    if (fact_number == FACTS_QUANTITY)
        this.battleEnd();
    else
        this.current_fact.next(fact_number);
  }

  battleEnd() {
    this.is_end.next(true);
    if (this.corrent.getValue() >= FACTS_QUANTITY / 2) {
        this.win_or_lost.next(true);
        this.status.wonBattle(this.rival_country.getValue());
    } else {
        this.win_or_lost.next(false);
        this.status.lost_battle(this.rival_country.getValue());
    }
  }

  changeFact() {
      let facts = this.facts.getValue();
      facts[this.current_fact.getValue()] = facts[FACTS_QUANTITY];
      this.facts.next(facts);
  }
}
