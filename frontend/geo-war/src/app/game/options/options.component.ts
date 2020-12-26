import { Component, OnInit } from '@angular/core';
import { GameStatusService } from '../status.service';

@Component({
  selector: 'options',
  templateUrl: './options.component.html',
  styleUrls: ['./options.component.css']
})
export class OptionsComponent implements OnInit {

  constructor(private status : GameStatusService) { }

  ngOnInit(): void {
  }

  startGame() {
    this.status.startGame();
  }

}
