%rebase('layout', title='Professores')

<h1>Gestão de Professores</h1>

<a href="/profs/add" class="btn btn-success" style="margin-bottom: 20px;">+ Novo Professor</a>

<table style="width: 100%; border-collapse: collapse;">
    <thead>
        <tr style="background-color: #3498db; color: white;">
            <th class="user-lists-header">ID</th>
            <th class="user-lists-header">Nome</th>
            <th class="user-lists-header">Email</th>
            <th class="user-lists-header">Data Nasc.</th>
            <th class="user-lists-header">Cargo</th>
            <th class="user-lists-header">Ações</th>
        </tr>
    </thead>
    <tbody>
        % for p in profs:
        <tr style="border-bottom: 1px solid #ddd;">
            <td style="padding: 10px;">{{p.id}}</td>
            <td style="padding: 10px;">{{p.name}}</td>
            <td style="padding: 10px;"><a href="mailto:{{p.email}}">{{p.email}}</a></td>
            <td style="padding: 10px;">{{p.birthdate}}</td>
            <td style="padding: 10px;">{{p.cargo}}</td>
            <td style="padding: 10px;">
                <button onclick="window.location.href='/profs/edit/{{p.id}}'" class="btn" style="background-color: #f39c12; margin-right: 5px;">Editar</button>
                <form action="/profs/delete/{{p.id}}" method="post" style="display: inline;" onsubmit="return confirm('Tem certeza que deseja excluir?')">
                    <button type="submit" class="btn btn-danger">Excluir</button>
                </form>
            </td>
        </tr>
        % end
    </tbody>
</table>
</section>