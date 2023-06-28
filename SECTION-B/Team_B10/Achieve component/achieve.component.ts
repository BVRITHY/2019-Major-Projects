import { Component,OnInit } from '@angular/core';
import { StudentService } from '../student.service';
@Component({
  selector: 'app-achieve',
  templateUrl: './achieve.component.html',
  styleUrls: ['./achieve.component.css']
})
export class AchieveComponent implements OnInit{
  Obj: any;
  user1: any;
  constructor(private service: StudentService) { }

  ngOnInit(): void {
    this.user1 = JSON.parse(localStorage.getItem("Users") || '{}');
    console.log("achieve.ts() " +this.user1.email);
  }

 
  seeClubs(){
    // console.log("inside seeClubs() "+this.user1.email);
    this.service.seeClubs(this.user1.email).subscribe((result)=>{this.checkObj(result)});
  }
  checkObj(users: any){
    if(users!==null){

      this.Obj = users;
      console.log("achieve.ts() " +this.Obj.ename);
    }
    else{
      alert("You didn't get any certificates yet!");    
    }
  }

  getAllCer(){
    return this.Obj.length;
  }
  getMeritCer(){
    return this.Obj.filter((Obj:any) => Obj.cer==='Merit').length;
  }
  getPartCer(){
    return this.Obj.filter((Obj:any) => Obj.cer==='Participation').length;
  }

  chocolateCountRadio :string='All';
  searchText:string='';

  onFilterRadio(data: string){
    this.chocolateCountRadio = data;
    console.log(this.chocolateCountRadio);
  }
  onSearchTextEntered(searchValue:string){
    this.searchText = searchValue;
    console.log(this.searchText);
  }
}
