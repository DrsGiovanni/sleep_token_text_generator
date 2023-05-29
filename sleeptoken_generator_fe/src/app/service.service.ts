import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ServiceService {

  constructor(private http: HttpClient) { }

  sendText(text: string) {
    console.log("mandio");
    let body = {
      testo: text
    }

    return this.http.post("http://127.0.0.1:2700", body, { responseType: 'blob' })
  }



}
