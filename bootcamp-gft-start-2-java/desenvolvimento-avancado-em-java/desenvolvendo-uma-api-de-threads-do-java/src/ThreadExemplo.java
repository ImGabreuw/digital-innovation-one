public class ThreadExemplo {

    public static void main(String[] args) {

        GeradorPDF geradorPDF = new GeradorPDF();
        BarraDeCarregamento barraDeCarregamento = new BarraDeCarregamento(geradorPDF);

        geradorPDF.start();
        barraDeCarregamento.start();
    }

}

class GeradorPDF extends Thread {

    @Override
    public void run() {
        try {
            System.out.println("Iniciando geração do PDF");

            Thread.sleep(5000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("PDF gerado");
    }

}

class BarraDeCarregamento extends Thread {

    private Thread geradorPDF;

    public BarraDeCarregamento(Thread geradorPDF) {
        this.geradorPDF = geradorPDF;
    }

    @Override
    public void run() {
        while (true) {
            try {
                Thread.sleep(500);

                if (!geradorPDF.isAlive()) break;

                System.out.println("Loading...");
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

}
