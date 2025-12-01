% rebase('layout', title='Lançar Faltas')

<h2>Lançar Faltas</h2>
<form method="post" action="/lancar_faltas">
    <label for="disciplina">Disciplina:</label>
    <input type="text" id="disciplina" name="disciplina" required><br>
    <label for="aluno">Aluno:</label>
    <input type="text" id="aluno" name="aluno" required><br>
    <label for="faltas">Quantidade de Faltas:</label>
    <input type="number" id="faltas" name="faltas" min="0" required><br>
    <button type="submit">Lançar Faltas</button>
</form>
