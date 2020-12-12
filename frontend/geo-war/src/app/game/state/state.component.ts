import { Component, OnInit } from '@angular/core';
import { StatusService } from '../status.service';

@Component({
  selector: 'game-state',
  templateUrl: './state.component.html',
  styleUrls: ['./state.component.css']
})
export class StateComponent implements OnInit {
  country: string;
  points: number;
  conquered: number;
  username: string;
  constructor(private status: StatusService) {
    this.country = this.username = '';
    this.points = this.conquered = 0;
  }

  ngOnInit(): void {
    this.status.countryModified.subscribe(country => this.country = country);
    this.status.conqueredMoified.subscribe(conquered => this.conquered = conquered);
    this.status.usernameModified.subscribe(username => this.username = username);
    this.status.pointsModified.subscribe(points => this.points = points);
  }
}
