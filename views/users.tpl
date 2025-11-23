%rebase('layout', title='Usuários')

<h1>Gestão de Usuários</h1>

<a href="/users/add" class="btn btn-success" style="margin-bottom: 20px;">+ Novo Usuário</a>

<table style="width: 100%; border-collapse: collapse;">
    <thead>
        <tr style="background-color: #3498db; color: white;">
            <th style="padding: 10px; text-align: left; border-bottom: 2px solid #2980b9;">ID</th>
            <th style="padding: 10px; text-align: left; border-bottom: 2px solid #2980b9;">Nome</th>
            <th style="padding: 10px; text-align: left; border-bottom: 2px solid #2980b9;">Email</th>
            <th style="padding: 10px; text-align: left; border-bottom: 2px solid #2980b9;">Data Nasc.</th>
            <th style="padding: 10px; text-align: left; border-bottom: 2px solid #2980b9;">Ações</th>
        </tr>
    </thead>
    <tbody>
        % for u in users:
        <tr style="border-bottom: 1px solid #ddd;">
            <td style="padding: 10px;">{{u.id}}</td>
            <td style="padding: 10px;">{{u.name}}</td>
            <td style="padding: 10px;"><a href="mailto:{{u.email}}">{{u.email}}</a></td>
            <td style="padding: 10px;">{{u.birthdate}}</td>
            <td style="padding: 10px;">
                <button onclick="window.location.href='/users/edit/{{u.id}}'" class="btn" style="background-color: #f39c12; margin-right: 5px;">Editar</button>
                <form action="/users/delete/{{u.id}}" method="post" style="display: inline;" onsubmit="return confirm('Tem certeza que deseja excluir?')">
                    <button type="submit" class="btn btn-danger">Excluir</button>
                </form>
            </td>
        </tr>
        % end
    </tbody>
</table>