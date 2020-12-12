import { Component, OnInit } from '@angular/core';
import { StatusService } from '../status.service';

@Component({
  selector: 'country-pick',
  templateUrl: './pick.component.html',
  styleUrls: ['./pick.component.css']
})
export class PickComponent implements OnInit {
  countries = [
      'Israel', 'Italy', 'Spain', 'Usa', 'Canada', 'France', 'Germany', 'Japan', 'Egypt',
      'Portugal', 'Brazil', 'Argentina', 'Scotland', 'Marocco', 'England', 'Russia'
  ]
  color = [
    'single-option-green', 'single-option-blue', 'single-option-red', 'single-option-yellow'
  ]

  constructor(private service: StatusService) { }

  ngOnInit(): void {
  }

  selectCountry(country: string) {
    this.service.selectCountry(country);
  }

}
