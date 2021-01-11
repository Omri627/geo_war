import { Component, OnInit } from '@angular/core';
import { CountriesSummary } from 'src/app/models/countries_summary';
import { GameSummary } from 'src/app/models/game_summary';
import { UserService } from 'src/app/services/users/user.service';

@Component({
  selector: 'user-scores',
  templateUrl: './scores.component.html',
  styleUrls: ['./scores.component.css']
})
export class ScoresComponent implements OnInit {
  scores: GameSummary[];
  countries_summary: CountriesSummary[];

  /* scores state */
  game_summary_section: boolean;
  countries_summary_section: boolean;

  constructor(private userService: UserService) {
      this.game_summary_section = true;
      this.countries_summary_section = false;
  }

  ngOnInit(): void {
      this.userService.scoresModified.subscribe(scores => this.scores = scores);
      this.userService.countriesSummaryModified.subscribe(countries_summary => this.countries_summary = countries_summary);
  }

  /******* Event Handlers *********/

  game_summary_click() {
      this.countries_summary_section = false;
      this.game_summary_section = true;
  }

  countries_summary_click() {
      this.countries_summary_section = true;
      this.game_summary_section = false;
  }

  delete_game_score(id) {
      this.userService.delete_game_score(id);
  }

}
