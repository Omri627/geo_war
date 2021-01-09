import { ComponentFactoryResolver, Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs/internal/BehaviorSubject';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ActionStatus } from './models/action_status';
import { UserInfo } from './models/user_info';
import { UserStatics } from './models/user_statics';
import { GameSummary } from './models/game_summary';
import { CountriesSummary } from './models/countries_summary';
import {UserRank} from "./models/user_rank";

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
  users_rank = new BehaviorSubject<UserRank[]>(null);

  countries_summary = new BehaviorSubject<CountriesSummary[]>(null);
  instructions_section = new BehaviorSubject<boolean>(false);
  user_ranks_section = new BehaviorSubject<boolean>(false);


  loggedModified = this.isLogged.asObservable();
  usernameModified = this.username.asObservable();
  emailModified = this.email.asObservable();
  staticsModified = this.statics.asObservable();
  latestModified = this.latest.asObservable();
  scoresModified = this.scores.asObservable();
  countriesSummaryModified = this.countries_summary.asObservable();
  topUsersRanksModified = this.users_rank.asObservable();

  instructionsModified = this.instructions_section.asObservable();
  userRanksModified = this.user_ranks_section.asObservable();


  constructor(private http: HttpClient) {
    if (localStorage.getItem('username') != null && localStorage.getItem('username') != 'null')
      this.username.next(localStorage.getItem('username'));
    if (this.username.getValue() != '') {
        this.notify_login(this.username.getValue());
    }
  }

  notify_login(username: string) {
    this.username.next(username);
    localStorage.setItem('username', username);
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

  reload_user_data() {
      this.notify_login(this.username.getValue());
  }

  notify_logout() {
    this.username.next('');
    this.isLogged.next(false);
    localStorage.removeItem('username');
  }

  register(username: string, email:string, password: string): Observable<ActionStatus> {
      let http_input = { 'username': username, 'email': email, 'password': password }
      return this.http.post<ActionStatus>(this.ROOT_URL + '/users', http_input);
  }

  is_exist(username: string) {
      return this.http.get<boolean>(this.ROOT_URL + '/users/exist/' + username);
  }

  display_instructions() {
      this.instructions_section.next(true);
      this.user_ranks_section.next(false);
  }

  display_user_ranks() {
      this.instructions_section.next(false);
      this.user_ranks_section.next(true);
  }

  close_sections() {
      this.instructions_section.next(false);
      this.user_ranks_section.next(false);
  }

  login(username: string, password: string) {
    const HTTP_OPTIONS = {
      headers: new HttpHeaders({
        'Access-Control-Allow-Credentials': 'true',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, PATCH, DELETE, PUT, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With',
      })
    };
    const http_input = {'username': username, 'password': password}
    return this.http.post<boolean>(this.ROOT_URL + '/users/login', http_input, HTTP_OPTIONS);
  }

  user_statics(username: string) {
      let statics = this.http.get<UserStatics>(this.ROOT_URL + '/user/statics/' + username);
      statics.subscribe(data => this.statics.next(data));
  }

  top_users_rank(limit: number) {
      let ranking = this.http.get<UserRank[]>(this.ROOT_URL + '/top/users/' + limit);
      ranking.subscribe(data => this.users_rank.next(data));
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

  addGameScore(country: string, points:number, conquered:number) {
    const HTTP_OPTIONS = {
      headers: new HttpHeaders({
        'Access-Control-Allow-Credentials': 'true',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, PATCH, DELETE, PUT, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With',
      })
    };
    const http_input = {'user_name': this.username.getValue(), 'country': country, 'points': points, 'conquered': conquered}
    let result = this.http.post<ActionStatus>(this.ROOT_URL + '/score/save', http_input, HTTP_OPTIONS);
    result.subscribe(response => {
        if (!response.valid)
            alert(response.error_message);
    });

    /* re-load user data */
    this.user_scores(this.username.getValue());
    this.user_latest(this.username.getValue());
    this.user_statics(this.username.getValue());
    this.user_countries_summary(this.username.getValue());
  }

  delete_game_score(game_id) {
    let delete_response = this.http.delete<ActionStatus>(this.ROOT_URL + '/delete/game/' + game_id);
    delete_response.subscribe(response => {
        if (response.valid) {
          alert('Selected game score have deleted successfully');
          this.reload_user_data();
        } else
          alert('Error: ' + response.error_message);
    });
  }
}
