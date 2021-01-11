import { Component, OnInit } from '@angular/core';
import { GameStatusService } from '../../services/game_status/status.service';
import { SelectService } from '../../services/select/select.service';

@Component({
  selector: 'country-pick',
  templateUrl: './pick.component.html',
  styleUrls: ['./pick.component.css']
})
export class PickComponent implements OnInit {
  countries: any;
  color: any;

  constructor(private service: GameStatusService, private select: SelectService) {
      this.color = [
        'single-option-green', 'single-option-blue', 'single-option-red', 'single-option-yellow'
      ]
      this.countries = []
  }

  ngOnInit(): void {
      this.select.fill_countries_options();
      this.select.countries.subscribe(countries_list => this.countries = countries_list);
  }

  /* Event triggered when the user selected a country */
  selectCountry(country: string) {
      this.service.selectCountry(country);
  }

}
