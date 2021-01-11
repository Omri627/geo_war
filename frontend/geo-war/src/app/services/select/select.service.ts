import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { GameStatusService } from '../game_status/status.service';

@Injectable({
  providedIn: 'root'
})
export class SelectService {
  readonly ROOT_URL = 'http://localhost:8000'
  countries: any;

  /* Service Constructor */
  constructor(private http: HttpClient) {
      this.countries = []
  }

  /* Send Server http request for list of countries that can be selected by user */
  fill_countries_options(): Observable<String[]>  {
    this.countries = this.http.get<String[]>(this.ROOT_URL + '/countries/select');
    return this.countries;
  }

}
