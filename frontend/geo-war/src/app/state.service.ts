import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs/internal/BehaviorSubject';

@Injectable({
  providedIn: 'root'
})
export class StateService {
  isLogged = new BehaviorSubject<boolean>(false);
  loggedModified = this.isLogged.asObservable();
  username: string;

  constructor() { 
    this.username = '';
  }

  login() {
    this.isLogged.next(true);
  }

  logout() {
    this.isLogged.next(false);
  }
}
