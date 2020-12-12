import { Component, OnInit } from '@angular/core';
import { StatusService } from '../status.service';

@Component({
  selector: 'intro',
  templateUrl: './intro.component.html',
  styleUrls: ['./intro.component.css']
})
export class IntroComponent implements OnInit {
  isCountryPicked: boolean;
  isStarted: boolean;
  constructor(private status : StatusService) {
    this.isCountryPicked = false;
    this.isStarted = false; 
  }

  ngOnInit(): void {
    this.status.countryPicked.subscribe(isCountryPicked => this.isCountryPicked = isCountryPicked);
    this.status.isStarted.subscribe(isStarted => this.isStarted = isStarted);
  }

  startGame() {
    this.status.startGame();
  }

}
