'use client';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import styles from './page.module.css'
import ContatosService from './services/contatos-service';

export default function Home() {
  
  function cadastrar(event: any): void {
    event.preventDefault();

    const { nome, telefone } = event.target;

    ContatosService.cadastrar({
      id: 0,
      nome: nome.value,
      telefone: telefone.value
    }).then((contato) => {
      console.log(contato);
    });
  }

  return (
    <main className={styles.main}>
      <Form onSubmit={cadastrar}>
        <Form.Group className="mb-3">
          <Form.Label>Nome</Form.Label>
          <Form.Control type="text" placeholder="Seu nome" name="nome"/>
        </Form.Group>

        <Form.Group className="mb-3">
          <Form.Label>Telefone</Form.Label>
          <Form.Control type="text" placeholder="Seu telefone" name="telefone"/>
        </Form.Group>
        <Button variant="primary" type="submit">
          Salvar
        </Button>
      </Form>
    </main>
  )
}
