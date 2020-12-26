import { Component } from '@angular/core';
import { UserService } from './user.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  isLogged : boolean;

  constructor(private state : UserService) {
    this.isLogged = true;
  }

  ngOnInit() {
    this.state.loggedModified.subscribe(isLogged => this.isLogged = isLogged);
  }
}
