import { Component, OnInit } from '@angular/core';
import { StatusService } from './status.service';

@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.css']
})
export class GameComponent implements OnInit {
  isStarted: boolean;
  isCountryPicked: boolean;
  inBattle: boolean;
  constructor(private status: StatusService) {
    this.isStarted = false;
    this.isCountryPicked = false;
    this.inBattle = false;
  }

  ngOnInit(): void {
    this.status.startedModified.subscribe(isStarted => this.isStarted = isStarted);
    this.status.countryPicked.subscribe(isCountryPicked => this.isCountryPicked = isCountryPicked);
    this.status.inBattle.subscribe(inBattle => this.inBattle = inBattle);
  }

}
