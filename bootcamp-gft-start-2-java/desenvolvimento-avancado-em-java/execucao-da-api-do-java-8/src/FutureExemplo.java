import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.*;
import java.util.stream.Collectors;

public class FutureExemplo {

    // Executors.newFixedThreadPool(3) => controle do número de thread em execução (Exemplo: caso as 3 threads já estejam em execcução, e foi chamado um 4º, então ela precisará esperar até alguma outra seja finalizada)
    private static final ExecutorService PESSOAS_PARA_EXECUTAR_ATIVIDADES = Executors.newFixedThreadPool(3);

    public static void main(String[] args) {
        Casa casa = new Casa(new Quarto());

        List<? extends Future<?>> futures = new CopyOnWriteArrayList<>(casa.obterAfazeresDaCasa())
                .stream()
                .map(atividade -> PESSOAS_PARA_EXECUTAR_ATIVIDADES.submit(atividade::realizar))
                .collect(Collectors.toList());

        while (futures.stream().allMatch(Future::isDone)) {
            int numeroDeAtividadesNaoFinalizadas = 0;

            for (Future<?> future : futures) {
                if (future.isDone()) {
                    try {
                        System.out.println("Parabéns! Você terminou de " + future.get());
                        futures.remove(future);
                    } catch (InterruptedException | ExecutionException e) {
                        e.printStackTrace();
                    }
                } else {
                    numeroDeAtividadesNaoFinalizadas++;
                }
            }

            System.out.println("Numero de atividades não finalizadas: " + numeroDeAtividadesNaoFinalizadas);
        }

        PESSOAS_PARA_EXECUTAR_ATIVIDADES.shutdown();
    }

}

class Casa {
    private List<Comodo> comodos;

    Casa(Comodo... comodos) {
        this.comodos = List.of(comodos);
    }

    List<Atividade> obterAfazeresDaCasa() {
        return comodos.stream()
                .map(Comodo::obterAfazeresDoComodo)
                .reduce(new ArrayList<>(), (pivo, atividade) -> {
                    pivo.addAll(atividade);
                    return pivo;
                });
    }
}

interface Atividade {

    void realizar();

}

abstract class Comodo {

    abstract List<Atividade> obterAfazeresDoComodo();

}

class Quarto extends Comodo {

    @Override
    List<Atividade> obterAfazeresDoComodo() {
        return List.of(
                this::arrumarGuardaRoupa,
                this::arrumarCana,
                this::arrumarQuarto
        );
    }

    private void arrumarGuardaRoupa() {
        try {
            Thread.sleep(5000);
            System.out.println("Arrumar o guarda roupa");
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    private void arrumarQuarto() {
        try {
            Thread.sleep(5000);
            System.out.println("Arrumar o quarto");
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

    }

    private void arrumarCana() {
        try {
            Thread.sleep(5000);
            System.out.println("Arrumar a cama");
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}