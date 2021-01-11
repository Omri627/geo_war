import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { ActionStatus } from 'src/app/models/action_status';
import { UserService } from 'src/app/services/users/user.service';

@Component({
  selector: 'signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {
  /* sign up form content */
  termsChecked: boolean;
  username: string;
  password: string;
  password_validation: string;
  email: string;

  /* error messages */
  terms_confirmation_error: string;
  username_error: string;
  password_error: string;
  email_error: string;
  success_message: string;
  server_error: string;
  is_password_error: boolean;

  /* elements references */
  @ViewChild("InputUsername") element_username: ElementRef;
  @ViewChild("InputEmail") element_email: ElementRef;
  @ViewChild("InputPassword") element_password: ElementRef;
  @ViewChild("InputVerification") element_verification: ElementRef;

  constructor(private state: UserService) {
      this.reset();
  }

  ngOnInit(): void { }

  reset(): void {
    this.username = this.password = this.password_validation = this.email = '';
    this.termsChecked = false;
    this.success_message = this.username_error = this.password_error = this.email_error = this.server_error = '';
    this.is_password_error = false;
  }

  /****** Events Handlers  ********/

  /* Event triggered when user clicked on terms confirmation check box */
  termsChanged() {
      this.termsChecked = !this.termsChecked;
      this.verify_terms();
  }

  verify_terms() {
    if (this.termsChecked)
      this.terms_confirmation_error = "";
    else
      this.terms_confirmation_error = 'You haven\'t confirmed the application terms';
  }

  verify_username() {
      if (this.username.length < 3) {
        this.username_error = "Username should be longer then 3 characters";
        this.element_username.nativeElement.classList.remove('success-input');
        this.element_username.nativeElement.classList.add('error-input');
      } else {
        this.username_error = ""
        this.element_username.nativeElement.classList.remove('error-input');
        this.element_username.nativeElement.classList.add('success-input');
        var action_status = this.state.is_exist(this.username);
        action_status.subscribe(is_exist => {
          if (is_exist) {
              this.username_error = 'This username is already exist';
              this.element_username.nativeElement.classList.remove('success-input');
              this.element_username.nativeElement.classList.add('error-input');
            }
        });
      }
  }

  verify_email() {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    let isValid = re.test(String(this.email).toLowerCase());
    if (!isValid) {
      this.email_error = "Email address has invalid format";
      this.element_email.nativeElement.classList.remove('success-input');
      this.element_email.nativeElement.classList.add('error-input');
    } else {
      this.email_error = "";
      this.element_email.nativeElement.classList.remove('error-input');
      this.element_email.nativeElement.classList.add('success-input');
    }
  }

  verify_password() {
    if (this.password.length < 3) {
      this.password_error = "Password should be longer then 3 characters";
      this.element_password.nativeElement.classList.remove('success-input');
      this.element_password.nativeElement.classList.add('error-input');
      this.is_password_error = true;
    } else {
      this.password_error = ""
      this.element_password.nativeElement.classList.remove('error-input');
      this.element_password.nativeElement.classList.add('success-input');
      this.is_password_error = false;
    }
    if (this.password_validation != '')
      this.verify_password_confirmation();
  }

  /* Event triggered when focusing out password textbox
    verifing that the password and password confimation is identical */
  verify_password_confirmation() {
    this.element_verification.nativeElement.classList.remove('form-login-normal');
    if (this.is_password_error) {
      this.element_verification.nativeElement.classList.remove('success-input');
      this.element_verification.nativeElement.classList.add('error-input');
    } else if (this.password != this.password_validation) {
        this.password_error = "Password confirmation isn't identical to password";
        this.element_verification.nativeElement.classList.remove('success-input');
        this.element_verification.nativeElement.classList.add('error-input');
    } else {
        this.password_error = "";
        this.element_verification.nativeElement.classList.remove('error-input');
        this.element_verification.nativeElement.classList.add('success-input');
    }
  }

  /* Event triggered when user clicked on register button */
  signUp() {
      this.verify_username();
      this.verify_email();
      this.verify_password();
      this.verify_password_confirmation();
      this.verify_terms();
      if (this.username_error != '' || this.email_error != '' || this.password_error != '' || this.termsChecked == false)
        return;

      var action_status = this.state.register(this.username, this.email, this.password);
      action_status.subscribe(action_status => {
          if (action_status.valid) {
            this.reset();
            this.success_message = action_status.error_message;
          } else
            this.server_error = action_status.error_message;
      });
  }

}
