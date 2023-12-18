import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CardModule } from 'primeng/card';
import ContatoService from '../services/contatos.service';
import { Contato } from '../models/contato.interface';
import { MessagesModule } from 'primeng/messages';
import { Message } from 'primeng/api';
import { ButtonModule } from 'primeng/button';
import { InputTextModule } from 'primeng/inputtext';

@Component({
  selector: 'cadastro',
  templateUrl: './cadastro.component.html',
  styleUrl: './cadastro.component.css',
  standalone: true,
  imports: [
    FormsModule,
    CardModule,
    MessagesModule,
    ButtonModule,
    InputTextModule
  ]
})
export class CadastroComponent {
  messages: Message[] = [];
  nome = '';
  telefone = '';

  public constructor(private service: ContatoService){};

  salvar(){
    const contato: Contato = {
      id: 0,
      nome: this.nome,
      telefone: this.telefone
    };

    this.service.salvar(contato).subscribe(() => {
      this.messages = [{
        severity: 'success',
        summary: 'Usuário cadastrado com sucesso'
      }];
      this.nome = '';
      this.telefone = '';
    });
  }
}
