import { Component, OnInit } from '@angular/core';
import { GameSummary } from 'src/app/models/game_summary';
import { UserService } from 'src/app/user.service';

@Component({
  selector: 'user-credentials',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent implements OnInit {
  /* user general data */
  username: string;
  email: string;

  /* statics data */
  games_played: number;
  total_points: number;
  total_conquered: number;
  top_country: string;

  /* latest game summary data */
  date_latest: string;
  country_latest: string;
  points_latest: number;
  conquered_latest: number;

  constructor(private userService: UserService) { 
  }

  ngOnInit(): void {
    this.userService.usernameModified.subscribe(username => this.username = username);
    this.userService.emailModified.subscribe(email => this.email = email);
    this.userService.staticsModified.subscribe(statics => {
        if (statics == null)
          return;
        this.games_played = statics.games_played;
        this.total_points = statics.total_points;
        this.top_country = statics.top_country;
        this.total_conquered = statics.total_conquered;
    })
    this.userService.latestModified.subscribe(latest => {
        if (latest == null)
          return;
        this.date_latest = latest.date.substring(0, 10);
        this.country_latest = latest.country;
        this.conquered_latest = latest.conquered;
        this.points_latest = latest.points;
    })

  }

}