import { ComponentFactoryResolver, Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs/internal/BehaviorSubject';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ActionStatus } from './models/action_status';
import { UserInfo } from './models/user_info';
import { UserStatics } from './models/user_statics';
import { GameSummary } from './models/game_summary';
import { CountriesSummary } from './models/countries_summary';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  readonly ROOT_URL = 'http://localhost:8000';
  isLogged = new BehaviorSubject<boolean>(false);
  username = new BehaviorSubject<string>('');
  email = new BehaviorSubject<string>('')
  statics = new BehaviorSubject<UserStatics>(null);
  latest = new BehaviorSubject<GameSummary>(null);
  scores = new BehaviorSubject<GameSummary[]>(null);
  countries_summary = new BehaviorSubject<CountriesSummary[]>(null);

  loggedModified = this.isLogged.asObservable();
  usernameModified = this.username.asObservable();
  emailModified = this.email.asObservable();
  staticsModified = this.statics.asObservable();
  latestModified = this.latest.asObservable();
  scoresModified = this.scores.asObservable();
  countriesSummaryModified = this.countries_summary.asObservable();

  constructor(private http: HttpClient) {
      if (this.username.getValue() != '') {
        this.notify_login(this.username.getValue());
      }
  }

  notify_login(username: string) {
    this.username.next(username);
    let user_credentials = this.http.get<UserInfo>(this.ROOT_URL + '/user/credentials/' + username);
    user_credentials.subscribe(user_credentials => {
        this.email.next(user_credentials.email);
    })
    this.isLogged.next(true);
    this.user_statics(username);
    this.user_latest(username);
    this.user_countries_summary(username);
    this.user_scores(username);
  }
  
  notify_logout() {
    this.username.next('');
    this.isLogged.next(false);
  }

  register(username: string, email:string, password: string): Observable<ActionStatus> {
      let http_input = { 'username': username, 'email': email, 'password': password }
      return this.http.post<ActionStatus>(this.ROOT_URL + '/users', http_input);
  }

  is_exist(username: string) {
      return this.http.get<boolean>(this.ROOT_URL + '/users/exist/' + username);
  }

  login(username: string, password: string) {
    const HTTP_OPTIONS = {
      headers: new HttpHeaders({
        'Access-Control-Allow-Credentials' : 'true',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, PATCH, DELETE, PUT, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With',
      })
    };
    const http_input = { 'username': username, 'password': password }
    return this.http.post<boolean>(this.ROOT_URL + '/users/login', http_input, HTTP_OPTIONS);
  }

  user_statics(username: string) {
      let statics = this.http.get<UserStatics>(this.ROOT_URL + '/user/statics/' + username);
      statics.subscribe(data => this.statics.next(data));
  }

  user_latest(username: string) {
      let statics = this.http.get<GameSummary>(this.ROOT_URL + '/user/latest/' + username);
      statics.subscribe(data => this.latest.next(data));
  }

  user_scores(username: string) {
      let scores = this.http.get<GameSummary[]>(this.ROOT_URL + '/user/scores/' + username);
      scores.subscribe(scores => this.scores.next(scores));
  }
  
  user_countries_summary(username: string) {
    let countries_summary = this.http.get<CountriesSummary[]>(this.ROOT_URL + '/user/countries/' + username);
    countries_summary.subscribe(countries_summary => this.countries_summary.next(countries_summary));
  }
}