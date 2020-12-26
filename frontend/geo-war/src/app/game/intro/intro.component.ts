import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/user.service';
import { GameStatusService } from '../status.service';

@Component({
  selector: 'intro',
  templateUrl: './intro.component.html',
  styleUrls: ['./intro.component.css']
})
export class IntroComponent implements OnInit {
  isCountryPicked: boolean;
  isStarted: boolean;
  username: string;
  constructor(private status : GameStatusService, private userService: UserService) {
    this.isCountryPicked = false;
    this.isStarted = false; 
  }

  ngOnInit(): void {
    this.status.countryPicked.subscribe(isCountryPicked => this.isCountryPicked = isCountryPicked);
    this.status.isStarted.subscribe(isStarted => this.isStarted = isStarted);
    this.userService.usernameModified.subscribe(username => this.username = username);
  }

  startGame() {
    this.status.startGame();
  }

}
