import { Component, OnInit } from '@angular/core';
import { GameStatusService } from '../status.service';
import {UserService} from "../../user.service";

@Component({
  selector: 'options',
  templateUrl: './options.component.html',
  styleUrls: ['./options.component.css']
})
export class OptionsComponent implements OnInit {

  constructor(private status: GameStatusService, private user_service: UserService) {
  }

  ngOnInit(): void {
  }

  startGame() {
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
