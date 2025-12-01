% rebase('layout', title='Turmas', nav_dict=nav_dict)

<div class="titulo">
    <h1>Minhas Turmas</h1>
    <p>Olá, Prof. {{prof.name}}! Gerencie suas disciplinas</p>
</div>

<!-- Seção: Turmas Inscritas -->
<h2>Minhas Turmas Inscritas</h2>
% if minhas_turmas:
<table class="table">
    <thead>
        <tr>
            <th>Código</th>
            <th>Nome</th>
            <th>Turma</th>
            <th>Horário</th>
            <th>Local</th>
        </tr>
    </thead>
    <tbody>
    % for d in minhas_turmas:
        <tr>
            <td>{{d.codigo}}</td>
            <td>{{d.nome}}</td>
            <td>{{d.turma}}</td>
            <td>{{d.horario}}</td>
            <td>{{d.local}}</td>
        </tr>
    % end
    </tbody>
</table>
% else:
<p>Você ainda não está inscrito em nenhuma turma.</p>
% end

<hr style="margin: 30px 0;">

<!-- Seção: Inscrever-se em Turmas -->
<h2>Se Inscrever na Turma</h2>
% if disponiveis:
<table class="table">
    <thead>
        <tr>
            <th>Código</th>
            <th>Nome</th>
            <th>Turma</th>
            <th>Período</th>
            <th>Local</th>
            <th>Ação</th>
        </tr>
    </thead>
    <tbody>
    % for d in disponiveis:
        <tr>
            <td>{{d.codigo}}</td>
            <td>{{d.nome}}</td>
            <td>{{d.turma}}</td>
            <td>{{d.ano_periodo}}</td>
            <td>{{d.local}}</td>
            <td>
                <form method="post" action="/visualizar_turmas" style="display:inline">
                    <input type="hidden" name="disciplina_id" value="{{d.id}}" />
                    <button type="submit">Inscrever-me</button>
                </form>
            </td>
        </tr>
    % end
    </tbody>
</table>
% else:
<p>Não há turmas disponíveis no momento.</p>
% end