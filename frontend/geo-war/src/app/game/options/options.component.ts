import { Component, OnInit } from '@angular/core';
import { GameStatusService } from '../../services/game_status/status.service';
import {UserService} from "../../services/users/user.service";

@Component({
  selector: 'options',
  templateUrl: './options.component.html',
  styleUrls: ['./options.component.css']
})
export class OptionsComponent implements OnInit {
  isStarted: boolean;
  constructor(private status: GameStatusService, private user_service: UserService) {
  }

  ngOnInit(): void {
    this.status.startedModified.subscribe(isStarted => this.isStarted = isStarted);
  }


  startGame() {
    var user_decision = true;
    if (this.isStarted)
      user_decision = confirm('Are you sure you want to start new game ?');
    if (user_decision)
      this.status.startGame();
  }

  instructions() {
    this.user_service.display_instructions();
  }

  top_ranks() {
      this.user_service.display_user_ranks();
  }

  exit() {
      this.user_service.notify_logout();
      window.scroll(0,0);
  }

}
