import { Component, OnInit } from '@angular/core';
import { StatusService } from '../status.service';

@Component({
  selector: 'options',
  templateUrl: './options.component.html',
  styleUrls: ['./options.component.css']
})
export class OptionsComponent implements OnInit {

  constructor(private status : StatusService) { }

  ngOnInit(): void {
  }

  startGame() {
    this.status.startGame();
  }

}
