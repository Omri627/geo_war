import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'topic',
  templateUrl: './topic.component.html',
  styleUrls: ['./topic.component.css']
})
export class TopicComponent implements OnInit {
  @Input() icon: string;
  @Input() color: string;
  @Input() title: string;
  @Input() description: string;
  title_class: string;
  icon_class: string;
  constructor() { 
    
  }

  ngOnInit(): void {
    this.icon_class = this.color + "-icon";
    this.title_class = this.color + "-topic-title";
  }


}
