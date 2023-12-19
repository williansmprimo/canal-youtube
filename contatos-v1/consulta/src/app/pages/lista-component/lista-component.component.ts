import { Component, OnInit } from '@angular/core';
import { Contato } from '../../model/contato.interface';
import ContatoService from '../../service/contatos.service';
import { TableModule } from 'primeng/table';
import { CardModule } from 'primeng/card';

@Component({
  selector: 'lista-contatos',
  standalone: true,
  imports: [
    TableModule,
    CardModule
  ],
  templateUrl: './lista-component.component.html',
  styleUrl: './lista-component.component.css'
})
export class ListaContatosComponent implements OnInit{
  listaContatos: Contato[] = [];

  constructor(private service: ContatoService){}

  ngOnInit(): void {
    this.service.listar().subscribe(resposta => {
      this.listaContatos = resposta;
    });
  }
}
