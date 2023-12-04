express = require('express');
mogoose = require('mongoose');
app = express();
app.use(express.json());
Contato = require('./contato');

// mogoose.connect('mongodb://127.0.0.0:27017');
mogoose.connect('mongodb://db-mongo:27017');

app.get('/contatos', async (req, res) => {
    console.log('get on /contatos');

    const contatos = await Contato.find();
    res.status(200).send(contatos);
});

app.get('/contatos/:id', async (req, res) => {
    console.log('get on /contatos/:id');

    const contato = await Contato.findOne({id: req.params.id});
    res.status(200).send(contato);
});

app.post('/contatos', async (req, res) => {
    console.log('post on /contatos');

    const contato = await Contato.create({
        id: req.body.id,
        nome: req.body.nome,
        telefone: req.body.telefone
    });
    res.status(200).send(contato);
});

app.listen(3000, () => {
    console.log('Server UP...');
});