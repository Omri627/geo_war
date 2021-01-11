import { HostListener, Component, OnInit } from '@angular/core';
import {UserService} from "../../services/users/user.service";
import {GameStatusService} from "../../services/game_status/status.service";

@Component({
  selector: 'navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
  isStarted: boolean;
  constructor(private user_service: UserService, private status: GameStatusService) {}

  ngOnInit(): void {
      this.status.startedModified.subscribe(isStarted => this.isStarted = isStarted);
  }

  @HostListener('window:scroll', ['$event']) onScrollEvent($event) {
    if (window.pageYOffset > 100) {
      document.getElementById('navbar').classList.add('scrolled');
    } else {
      document.getElementById('navbar').classList.remove('scrolled');
    }
  }

  logout() {
      this.user_service.notify_logout();
      window.scroll(0, 0);
  }

  startGame() {
    var user_decision = true;
    if (this.isStarted)
      user_decision = confirm('Are you sure you want to start new game ?');
    if (user_decision)
      this.status.startGame();
  }

  instructions() {
    this.user_service.display_instructions();
  }

  top_ranks() {
      this.user_service.display_user_ranks();
  }

  can_show() {
    if (this.isStarted)
      alert("cannot be displayed in middle of game");
  }
}
