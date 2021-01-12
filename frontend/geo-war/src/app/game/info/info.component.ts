import { Component, OnInit } from '@angular/core';
import {UserService} from "../../services/users/user.service";
import {UserRank} from "../../models/user_rank";
import {TOP_USERS_RANKS} from "../../services/rules";

@Component({
  selector: 'game-info',
  templateUrl: './info.component.html',
  styleUrls: ['./info.component.css']
})
export class InfoComponent implements OnInit {
  instructions_section: boolean;
  user_ranks_section: boolean;
  update_section: boolean;
  users_ranks: UserRank[];

  /* Used for update */
  username: string;
  password: string;
  email: string;
  password_validation: string;

  constructor(private user_service: UserService) {
    this.password = this.email = this.password_validation = '';
  }

  ngOnInit(): void {
      this.user_service.usernameModified.subscribe(username => this.username = username);
      this.user_service.instructionsModified.subscribe(instructions_section => this.instructions_section = instructions_section);
      this.user_service.userRanksModified.subscribe(user_ranks_section => this.user_ranks_section = user_ranks_section);
      this.user_service.updateSectionModified.subscribe(update_section => this.update_section = update_section)
      this.user_service.top_users_rank(TOP_USERS_RANKS);
      this.user_service.topUsersRanksModified.subscribe(users_ranks => this.users_ranks = users_ranks);
      this.email = this.user_service.email.getValue();
  }

  close_section() {
      this.user_service.close_sections();
  }

  update_info() {
      const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      const isValidEmail = re.test(String(this.email).toLowerCase());
      if (this.password.length < 3) {
        alert('Password should be longer then 3 characters');
        this.password = '';
        this.password_validation = '';
      } else if (this.password != this.password_validation) {
          alert('Password confirmation isn\'t identical to password');
          this.password = '';
          this.password_validation = '';
      } else if (!isValidEmail) {
          alert('The email address you have applied is not valid');
          this.email = '';
     } else {
        this.user_service.update_credentials(this.email, this.password);
        this.password = '';
        this.password_validation = '';
        this.email = '';
     }
  }

}
