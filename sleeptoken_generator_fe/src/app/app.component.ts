import { Component, OnInit } from '@angular/core';
import domtoimage from 'dom-to-image';
import { saveAs } from 'file-saver';
// import * as html2canvas from 'html2canvas'; // Importa html2canvas
import html2canvas from 'html2canvas';
import { FormControl, FormGroup } from '@angular/forms'
import { ServiceService } from './service.service';




@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'sleeptoken_generator_fe';
  risposta = ""
  imageSrc: any

  constructor(private service: ServiceService) { }
  imagePaths: string[] = [];
  testo = new FormControl('')

  ngOnInit() {
    const numImages = 2; // Numero totale di immagini nella sequenza
    for (let i = 0; i <= numImages; i++) {
      let num = ""
      switch (i) {
        case (0): num = "a"
          break;
        case (1): num = "b"
          break;
        case (2): num = "c"
          break;
      }
      const imagePath = `assets/images/${num}.png`;
      this.imagePaths.push(imagePath);
    }
  }


  downloadImage() {
    const element = document.getElementById('image-sequence') as HTMLElement;
    html2canvas(element).then((canvas) => {
      const imgData = canvas.toDataURL('image/png');
      const link = document.createElement('a');
      link.download = 'combined-image.png';
      link.href = imgData;
      link.click();
    });
  }

  sendText() {
    console.log("aaa");
    console.log(this.testo.value);


    if (this.testo.value) {
      this.service.sendText(this.testo.value).subscribe((response: any) => {
        const blob = new Blob([response], { type: 'image/jpeg' });
        const urlCreator = window.URL || window.webkitURL;
        const imageUrl = urlCreator.createObjectURL(blob);

        // Utilizza l'URL dell'immagine per visualizzarla o eseguire altre operazioni
        // ad esempio, assegnalo a una variabile nel tuo componente
        this.imageSrc = imageUrl;
      }, error => {
        console.error('Errore durante la richiesta:', error);
      });
    }
  }



}
