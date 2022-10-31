<h1>
Pylon Framework
</h1>
<hr/>
<p>
<strong>Pylon framework</strong> is based on the Flask tool. Pylon is created to facilitate the development of web systems or APIs.
leading to rapid development.
Pylon can adapted to various patterns like MVC, repository pattern or somthing similar.
</p>
<hr/>
<h2>How to run project?</h2>
<code> python app.py or flask run</code>
<p>
You need a .env file inside of project to define <code>FLASK_ENV</code> variable.
</p>
<h2>Scafolding</h2>
<div>
  <table>
     <thead>
       <tr>
         <td>Folder</td>
         <td>Description</td>
       </tr>
    </thead>
    <tbody>
      <tr>
        <td>
          src
        </td>
        <td>
          Source code
        </td>
      </tr>
       <tr>
        <td>
          src/middlewares
        </td>
        <td>
          Middleware directory contains all functions that execute before each requests for each endpoint
        </td>
      </tr>
       <tr>
        <td>
          src/modules
        </td>
        <td>
         <p>
            Modules directory contains all subdirectories modules. </br>
          For example:
          <code>
            src/modules/user/usercontroller.py
         </code>
          You can create manually 
           the controller or you can run pylon file with parameters.  </br>
        For example:
         
        <code>python pylon -c user -f user -d user</code>
          </p>
        </td>
      </tr>
      <tr>
        <td>
          src/routes
        </td>
        <td>
          routes for your application. <br> /api or / or you can add a new prefix.
        </td>
      </tr>
    </tbody>
  </table>
</div>
<hr/>
<h3>
Config
</h3>

