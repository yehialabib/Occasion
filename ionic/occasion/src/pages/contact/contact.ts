import { Component } from '@angular/core';

import { NavController } from 'ionic-angular';
@Component({
  selector: 'page-contact',
  templateUrl: 'contact.html'
})

export class ContactPage {
  list : any;
  constructor(public navCtrl: NavController) {
  }
  ngOnInit(){
     this.list=['ahmed','youssef','khaled','mostafa','alaa','mahmoud'];
   }
 }
