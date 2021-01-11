import { StylesCompileDependency, ThrowStmt } from '@angular/compiler';
import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { CountryGame } from 'src/app/models/country_game';
import { Fact } from 'src/app/models/fact';
import { BattleService } from 'src/app/services/battle/battle.service';
import { FACTS_QUANTITY, SHOW_ANSWER_WAIT_TIME, SHOW_BATTLE_SUMMARY_WAIT_TIME } from 'src/app/services/rules';
import { GameStatusService } from '../../services/game_status/status.service';

@Component({
  selector: 'game-fact',
  templateUrl: './fact.component.html',
  styleUrls: ['./fact.component.css']
})
export class FactComponent implements OnInit {
  user_country: string;
  rival_country: CountryGame;
  fact_number: number;
  correct: number;
  facts_total: number;
  facts: Fact[];
  lives: number;
  aboutWinOrLose: boolean;
  revealAsnwer: boolean;
  hint: boolean;
  revealAnswerEnable: boolean;
  hintEnable: boolean;
  changeFactEnable: boolean;

  /* indicate wether to show the answer or not in the moment */
  show_answer: boolean;
  right_or_wrong: boolean;

  /* user messages */
  battle_over_message: string;
  current_correct_message: number;
  current_wrong_message: number;
  correct_answer_messages = [ 'Well Done!, you were right', 'That\'s correct !', 'Correct ! keep on']
  wrong_answer_messages = [ 'That\'s wrong', 'Your were incorrect' ]
  @ViewChild("Correct") element_correct: ElementRef;
  @ViewChild("Incorrect") element_incorrect: ElementRef;
  @ViewChild("FullDetailedAsnwer") element_detailed_asnwer: ElementRef;
  @ViewChild("TrueButton") true_button: ElementRef;
  @ViewChild("FalseButton") false_button: ElementRef;


  constructor(private battleService : BattleService, private status: GameStatusService) {
      this.facts_total = FACTS_QUANTITY;
      this.show_answer = false;
      this.right_or_wrong = false;
      this.battle_over_message = '';
      this.current_correct_message = this.current_wrong_message = 0;
      this.revealAsnwer = false;
  }

  ngOnInit(): void {
      this.battleService.user_country.subscribe(country => this.user_country = country);
      this.battleService.rival_country.subscribe(country => this.rival_country = country);
      this.battleService.corrent.subscribe(correct => this.correct = correct);
      this.battleService.current_fact.subscribe(fact_number => this.fact_number = fact_number);
      this.battleService.facts.subscribe(facts => this.facts = facts);
      this.status.hintModified.subscribe(hintEnable => this.hintEnable = hintEnable);
      this.status.revealModified.subscribe(revealAnswerEnable => this.revealAnswerEnable = revealAnswerEnable);
      this.status.changeFactModified.subscribe(changeFactEnable => this.changeFactEnable = changeFactEnable);
      this.status.livesModified.subscribe(lives => this.lives = lives);
  }

  getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
  }

  random_feedback_messages() {
      this.current_correct_message = this.getRandomInt(0, this.correct_answer_messages.length);
      this.current_wrong_message = this.getRandomInt(0, this.wrong_answer_messages.length);
  }

  assignAnswer(answer: boolean): void {
      let awaiting_time = SHOW_ANSWER_WAIT_TIME;
      this.random_feedback_messages();
      this.show_answer = true;
      if (answer == this.facts[this.fact_number].answer)
        this.right_or_wrong = true;
      else
        this.right_or_wrong = false;
      if (this.fact_number == FACTS_QUANTITY - 1) {
          awaiting_time = SHOW_BATTLE_SUMMARY_WAIT_TIME;
          if (this.correct >= FACTS_QUANTITY / 2 || (this.right_or_wrong && this.correct + 1 >= FACTS_QUANTITY / 2)) {
              this.battle_over_message = "Good job! You won the battle against " + this.rival_country.name + " and took control of its land. The changes will take effect in the game world map";
              this.aboutWinOrLose = true;
            } else {
              this.aboutWinOrLose = false;
              if (this.status.is_live_descrease())
                this.battle_over_message = "You lost the battle. The country " + this.rival_country.name + " counterattacked your nation. Luckly they didn't manage to subdue your state or occupied part of your territory, however their attack caused damage and left you with solely " + (this.lives - 1) + " lives in total. ";
              else
                this.battle_over_message = "You lost the battle. The country " + this.rival_country.name + " counterattacked your nation and occupied part of your territory. The changes will take effect in the game world map.";
          }
      }
      this.true_button.nativeElement.hidden = true;
      this.false_button.nativeElement.hidden = true;
      setTimeout(() => {
          this.show_answer = false;
          this.battleService.assignAnswer(answer);
          this.battle_over_message = "";
          this.hint = this.revealAsnwer = false;
          this.true_button.nativeElement.hidden = false;
          this.false_button.nativeElement.hidden = false;
      }, awaiting_time);
  }

  revealAnswerAction() {
    this.revealAsnwer = true;
    this.status.useRevealAnswer();
  }

  hintAction() {
    this.hint = true;
    this.status.useHint();
  }

  changeFactAction() {
    this.status.useChangeFact();
    this.battleService.changeFact();
  }

}
