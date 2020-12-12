import { Component } from '@angular/core';
import { StateService } from './state.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  state : StateService;
  isLogged : boolean;

  constructor(state : StateService) {
    this.state = state;
    this.isLogged = true;
  }

  ngOnInit() {
    this.state.loggedModified.subscribe(isLogged => this.isLogged = isLogged);
  }
}
