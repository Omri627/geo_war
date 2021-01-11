import { TestBed } from '@angular/core/testing';

import { GameStatusService } from './status.service';

describe('StatusService', () => {
  let service: GameStatusService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GameStatusService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
