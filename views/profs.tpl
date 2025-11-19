%rebase('layout', title='Professores')

<section class="profs-section">
    <div class="section-header">
        <h1 class="section-title"><i class="fas fa-chalkboard-teacher"></i> Gestão de Professores</h1>
        <a href="/profs/add" class="btn btn-primary">
            <i class="fas fa-plus"></i> Novo Professor
        </a>
    </div>

    <div class="table-container">
        <table class="styled-table">
            
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>Email</th>
                    <th>Data Nasc.</th>
                    <th>Cargo</th>
                    <th>Ações</th>
                </tr>
            </thead>

            <tbody>
                % for p in profs:
                <tr>
                    <td>{{p.id}}</td>
                    <td>{{p.name}}</td>
                    <td><a href="mailto:{{p.email}}">{{p.email}}</a></td>
                    <td>{{p.birthdate}}</td>
                    <td>{{p.cargo}}</td>
                    
                    <td class="actions">
                        <button type="button" onclick="window.location.href='/profs/edit/{{p.id}}'" class="btn btn-sm btn-primary">
                            <i class="fas fa-edit"></i> Editar
                        </button>

                        <form action="/profs/delete/{{p.id}}" method="post" 
                              onsubmit="return confirm('Tem certeza?')">
                            <button type="submit" class="btn btn-sm btn-danger">
                                <i class="fas fa-trash-alt"></i> Excluir
                            </button>
                        </form>
                    </td>
                </tr>
                % end
            </tbody>
        </table>
    </div>
</section>