import { Component } from '@angular/core';

@Component({
  selector: 'app-counter',
  template: `
    <div>
      <h2>Counter</h2>
      <button (click)="increment()">Increment</button>
      <span>{{ count }}</span>
      <button (click)="decrement()">Decrement</button>
    </div>
  `,
  styleUrls: ['./counter.component.css']
})
export class CounterComponent {
  count = 0;

  increment() {
    this.count++;
  }

  decrement() {
    this.count--;
  }
}
