import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs/internal/BehaviorSubject';

@Injectable({
  providedIn: 'root'
})
export class StatusService {
  country = new BehaviorSubject<string>('');
  username = new BehaviorSubject<string>('');
  points = new BehaviorSubject<number>(0);
  conquered = new BehaviorSubject<number>(0);
  isStarted = new BehaviorSubject<boolean>(false);
  isCountryPicked = new BehaviorSubject<boolean>(false);
  inBattle = new BehaviorSubject<boolean>(false);

  countryModified = this.country.asObservable();
  usernameModified = this.username.asObservable();
  pointsModified = this.points.asObservable();
  conqueredMoified = this.conquered.asObservable();
  startedModified = this.isStarted.asObservable();
  countryPicked = this.isCountryPicked.asObservable();
  battleStatus = this.inBattle.asObservable();
  
  constructor() {}

  startGame() {
    this.isStarted.next(true);
  }

  endGame() {
    this.isStarted.next(false);
  }

  selectCountry(country: string) {
    this.country.next(country);
    this.isCountryPicked.next(true);
  }

  disselectCountry() {
    this.country.next('');
    this.isCountryPicked.next(false);
  }

  defeatCountry(points: number) {
    this.points.next(this.points.getValue() + points);
    this.conquered.next(this.conquered.getValue() + 1);
    this.inBattle.next(false);
  }

  battle() {
    this.inBattle.next(true);
  }

  endBattle() {
    this.inBattle.next(false);
  }

}
