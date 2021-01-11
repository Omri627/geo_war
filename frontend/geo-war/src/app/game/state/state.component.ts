import { Component, OnInit } from '@angular/core';
import { LIVES_QUANTITY } from 'src/app/services/rules';
import { UserService } from 'src/app/services/users/user.service';
import { GameStatusService } from '../../services/game_status/status.service';


@Component({
  selector: 'game-state',
  templateUrl: './state.component.html',
  styleUrls: ['./state.component.css']
})
export class StateComponent implements OnInit {
  country: string;
  points: number;
  conquered: number;
  max_conquered: number;
  username: string;
  isStarted: boolean;
  lives: number;

  /* helpers */
  changeFact: boolean;
  revealAnswer: boolean;
  hint: boolean;

  constructor(private userService: UserService, private status: GameStatusService) {
    this.country = '';
    this.points = this.conquered = 0;
    this.isStarted = false;
    this.lives = LIVES_QUANTITY;
  }

  ngOnInit(): void {
    this.status.countryModified.subscribe(country => this.country = country);
    this.status.conqueredMoified.subscribe(conquered => this.conquered = conquered);
    this.status.pointsModified.subscribe(points => this.points = points);
    this.status.isStarted.subscribe(isStarted => this.isStarted = isStarted);
    this.status.livesModified.subscribe(lives => this.lives = lives);
    this.status.maxConqueredModified.subscribe(max_conquered => this.max_conquered = max_conquered);
    this.userService.usernameModified.subscribe(username => this.username = username);
    this.status.hintModified.subscribe(hint => this.hint = hint);
    this.status.changeFactModified.subscribe(changeFact => this.changeFact = changeFact);
    this.status.revealModified.subscribe(revealAnswer => this.revealAnswer = revealAnswer);
  }
}
