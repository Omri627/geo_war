import { Component, OnInit } from '@angular/core';
import {UserService} from "../../user.service";
import {UserRank} from "../../models/user_rank";

@Component({
  selector: 'game-info',
  templateUrl: './info.component.html',
  styleUrls: ['./info.component.css']
})
export class InfoComponent implements OnInit {
  instructions_section: boolean;
  user_ranks_section: boolean;
  top_quantity: number;
  users_ranks: UserRank[];

  constructor(private user_service: UserService) {
      this.top_quantity = 10;
  }

  ngOnInit(): void {
      this.user_service.instructionsModified.subscribe(instructions_section => this.instructions_section = instructions_section);
      this.user_service.userRanksModified.subscribe(user_ranks_section => this.user_ranks_section = user_ranks_section);
      this.user_service.top_users_rank(this.top_quantity);
      this.user_service.topUsersRanksModified.subscribe(users_ranks => this.users_ranks = users_ranks);
  }

  close_section() {
      this.user_service.close_sections();
  }

}
