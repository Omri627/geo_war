import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { StatusService } from '../status.service';

@Component({
  selector: 'game-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit {
  countries = [
    'Israel', 'Italy', 'Spain', 'Usa', 'Canada', 'France', 'Germany', 'Japan', 'Egypt',
    'Portugal', 'Brazil', 'Argentina', 'Scotland', 'Marocco', 'England', 'Russia'
  ]
  constructor(private status : StatusService) {}

  ngOnInit(): void {}

  battleCountry() {
    this.status.battle();
  }

}
