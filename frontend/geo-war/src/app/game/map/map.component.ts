import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { CountryGame } from 'src/app/models/country_game';
import { BattleService } from 'src/app/services/battle/battle.service';
import { GameStatusService } from '../status.service';

@Component({
  selector: 'game-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit {
  countries = [];
  hover_id: number;
  user_country: string;

  @ViewChild("Intro") element_intro: ElementRef;

  constructor(private status : GameStatusService, private battleService: BattleService) {
    this.hover_id = -1;
  }

  ngOnInit(): void {
      this.status.countryModified.subscribe(country => this.user_country = country);
      this.status.select_rival_countries();
      this.status.countries.subscribe(countries_list => this.countries = countries_list);
      setTimeout(() => {
        this.element_intro.nativeElement.classList.add('game-introductory');
      }, 5000);
      setTimeout(() => {
        this.element_intro.nativeElement.classList.add('intro-hide');
      }, 15000);
  }

  battleCountry(rival_country: CountryGame) {
      this.status.battleState();
      this.battleService.startBattle(this.user_country, rival_country);
  }

  /* presentation methods */
  get_country_id(id: number) {
      return 'country-' + id;
  }

  get_country_text_id(id: number) {
      return 'country-n' + id;
  }

  get_country_color_id(id: number) {
      if (this.countries[id - 1].isConquered == true)
        return 'user-country-color';
      return 'country-' + id + '-color';
  }

  get_crown_position_id(id: number) {
      return "crown-icon-wrapper-" + id;
  }

  display(name: string) {
      if (name == 'United States')
        return 'USA';
      if (name == 'United Kingdom')
        return 'England';
      return name;
  } 

  notify_hover(i) {
      this.hover_id = i;
      window.onkeyup = function(hover_id: number, countries: any, status: GameStatusService) {
        var event_handler = function(e) {
        console.log("on key up    " + e.keyCode + " " + hover_id);
        if (hover_id == -1)
          return;
        if (e.keyCode == 87 || e.keyCode == 119) {
              status.wonBattle(countries[hover_id]);
          } else if (e.keyCode == 76 || e.keyCode == 108) {
              status.lost_battle(countries[hover_id]);
          }
        }
        return event_handler;
      }(this.hover_id, this.countries, this.status);
  }

  disable_hover() {
      this.hover_id = -1;
      window.onkeyup = function(e) {}
  }

}
