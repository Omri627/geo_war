import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { UpperComponent } from './login/upper/upper.component';
import { InstructionsComponent } from './login/instructions/instructions.component';
import { TopicsComponent } from './login/topics/topics.component';
import { FooterComponent } from './login/footer/footer.component';
import { DataComponent } from './login/data/data.component';
import { SignupComponent } from './login/signup/signup.component';
import { TopicComponent } from './login/topic/topic.component';
import { GallaryComponent } from './login/gallary/gallary.component';
import { SigninComponent } from './login/signin/signin.component';
import { GameComponent } from './game/game.component';
import { NavbarComponent } from './game/navbar/navbar.component';
import { OptionsComponent } from './game/options/options.component';
import { StateComponent } from './game/state/state.component';
import { MapComponent } from './game/map/map.component';
import { IntroComponent } from './game/intro/intro.component';
import { BannerComponent } from './game/banner/banner.component';
import { BottomComponent } from './game/bottom/bottom.component';
import { GameStatusService } from './game/status.service';
import { PickComponent } from './game/pick/pick.component';
import { FactComponent } from './game/fact/fact.component';
import { SelectService } from './game/pick/select.service';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { UserService } from './user.service';
import { UserComponent } from './game/user/user.component';
import { ScoresComponent } from './game/scores/scores.component';
import { EndgameComponent } from './game/endgame/endgame.component';
import { InfoComponent } from './game/info/info.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    UpperComponent,
    InstructionsComponent,
    TopicsComponent,
    FooterComponent,
    DataComponent,
    SignupComponent,
    TopicComponent,
    GallaryComponent,
    SigninComponent,
    GameComponent,
    NavbarComponent,
    OptionsComponent,
    StateComponent,
    MapComponent,
    IntroComponent,
    BannerComponent,
    BottomComponent,
    PickComponent,
    FactComponent,
    UserComponent,
    ScoresComponent,
    EndgameComponent,
    InfoComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [
    UserService,
    GameStatusService,
    SelectService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
