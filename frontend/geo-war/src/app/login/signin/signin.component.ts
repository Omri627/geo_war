import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/user.service';

@Component({
  selector: 'signin',
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.css']
})
export class SigninComponent implements OnInit {
  username: string;
  password: string;
  error_message: string;
  constructor(private state : UserService) { 
      this.error_message = "";
      this.username = this.password = '';
  }

  ngOnInit(): void {

  }

  login() {
    console.log(this.username);
    if (this.username == '' || this.password == '') {
        this.error_message = "Fill in your credentials to log in";
        return;
    }
    var response = this.state.login(this.username, this.password);
    response.subscribe(islogged => {
        if (islogged) {
          window.scroll(0,0);
          this.state.notify_login(this.username);
        } else 
          this.error_message = "The username or password you have entered is incorrect"
    })
  }



}
