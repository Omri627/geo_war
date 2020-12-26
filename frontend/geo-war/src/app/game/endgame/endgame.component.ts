import { Component, OnInit } from '@angular/core';
import { GameStatusService } from '../status.service';

@Component({
  selector: 'endgame',
  templateUrl: './endgame.component.html',
  styleUrls: ['./endgame.component.css']
})
export class EndgameComponent implements OnInit {
  winOrLose: boolean;
  points: number;
  country: string;
  max_conquered: number;
  
  constructor(private status: GameStatusService) { }

  ngOnInit(): void {
    this.status.winOrLoseModified.subscribe(winOrLose => this.winOrLose = winOrLose);
    this.status.pointsModified.subscribe(points => this.points = points);
    this.status.countryModified.subscribe(country => this.country = country);
    this.status.maxConqueredModified.subscribe(max_conquered => this.max_conquered = max_conquered);
  }

  main_menu_click() {
      this.status.startGame();
      this.status.isStarted.next(false);
  }

  new_game() {
      this.status.startGame();
  }

}
