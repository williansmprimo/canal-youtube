#include <stdio.h>
#include <stdlib.h>

struct ITEM {
    int valor;
    struct ITEM* prox;
};
typedef struct ITEM ITEM;

struct LISTA {
    ITEM* inicio;
    ITEM* ultimo;
};
typedef struct LISTA LISTA;

ITEM* criarITEM(int valor){
    ITEM* item = (ITEM*)malloc(sizeof(ITEM));
    item->valor = valor;
    item->prox = NULL;
    return item;
}

LISTA criarLista(){
    LISTA lista;
    lista.inicio = criarITEM(-1);
    lista.ultimo = lista.inicio;
    return lista;
}

void listar(ITEM* inicio){
    ITEM* atual = inicio->prox;
    while(atual != NULL){
        printf("->(%d)", atual->valor);
        atual = atual->prox;
    }
    printf("\n");
}

ITEM* buscar(ITEM* inicio, int valor){
    ITEM* atual = inicio->prox;
    while(atual != NULL){
        if(atual->valor == valor){
            return atual;
        }
        atual = atual->prox;
    }
    return NULL;
}

void remover(ITEM* inicio, int valor){
    ITEM* atual = inicio->prox;
    ITEM* anterior = inicio;
    while(atual != NULL){
        if(atual->valor == valor){
            anterior->prox = atual->prox;
            free(atual);
            return;
        }
        anterior = atual;
        atual = atual->prox;
    }
}

ITEM* inserir(LISTA* lista, ITEM* novo){
    novo->prox = lista->ultimo->prox;
    lista->ultimo->prox = novo;
    lista->ultimo = novo;
    return novo;
}

int main(){
    LISTA lista = criarLista();

    int valor;
    int opcao; //0 - sair, 1 - inserir, 2 - buscar e 3 - remover
    while(1){
        printf("\n0 - sair, 1 - inserir, 2 - buscar e 3 - remover, 4 - listar:");
        scanf("%d", &opcao);
        if(opcao == 0){
           break;
        }else if(opcao == 1){
            printf("Digite o valor a inserir:");
            scanf("%d", &valor);
            inserir(&lista, criarITEM(valor));
        }else if(opcao == 2){
            printf("Digite o valor a buscar:");
            scanf("%d", &valor);
            if(buscar(lista.inicio, valor) != NULL){
                printf("O valor existe!");
            }
        }else if(opcao == 3){
            printf("Digite o valor a remover:");
            scanf("%d", &valor);
            remover(lista.inicio, valor);
        }else {
            listar(lista.inicio);
        }
    }

    return 0;
}
