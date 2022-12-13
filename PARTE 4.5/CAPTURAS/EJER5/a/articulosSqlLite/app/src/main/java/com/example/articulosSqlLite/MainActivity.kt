package com.example.sqllite14_11_22

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.view.View
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView.Adapter
import com.example.sqllite14_11_22.adapter.UsuariosAdapter
import com.example.sqllite14_11_22.databinding.ActivityMainBinding
import com.example.sqllite14_11_22.db.BaseDatos
import com.example.sqllite14_11_22.models.Usuarios

class MainActivity : AppCompatActivity() {
    lateinit var binding: ActivityMainBinding

    lateinit var conexion: BaseDatos
    lateinit var adapter: UsuariosAdapter
    var lista = mutableListOf<Usuarios>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        conexion = BaseDatos(this)
        setRecycler()
        setListeners()
    }

    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        menuInflater.inflate(R.menu.menu_opciones, menu)
        return super.onCreateOptionsMenu(menu)
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return when(item.itemId){
            R.id.item_crear->{
                startActivity(Intent(this, AddUpdateActivity::class.java))
                true
            }
            R.id.item_borrar_todo->{
                conexion.borrarTodo()
                lista.clear()
                adapter.notifyDataSetChanged()
                binding.tvNo.visibility = View.VISIBLE

                true
            }
            R.id.item_salir->{
                finish()
                true
            }
            else->true
        }
    }

    private fun setListeners() {
        binding.fabAdd.setOnClickListener {
            startActivity(Intent(this, AddUpdateActivity::class.java))
        }
    }

    private fun setRecycler() {
        lista = conexion.readAll()
        binding.tvNo.visibility = View.INVISIBLE
        if (lista.size == 0) {
            binding.tvNo.visibility = View.VISIBLE
            return
        }

        val layoutManager = LinearLayoutManager(this)
        binding.recUsuarios.layoutManager = layoutManager
        adapter = UsuariosAdapter(lista, { onItemDelete(it) }) {
            usuario->onItemUpdate(usuario)
        }
        binding.recUsuarios.adapter = adapter
    }

    private fun onItemUpdate(usuario: Usuarios) {
        //pasamos el usuario al activity updatecreate
        val i = Intent(this, AddUpdateActivity::class.java).apply {
            putExtra("USUARIO", usuario)
        }
        startActivity(i)
    }

    private fun onItemDelete(position: Int) {
        val usuario = lista[position]
        conexion.borrar(usuario.id)
        //borramos de la lista e indicamos al adapter que hemos
        //eliminado un gristro
        lista.removeAt(position)
        if (lista.size == 0) {
            binding.tvNo.visibility = View.VISIBLE
        }
        adapter.notifyItemRemoved(position)

    }

    override fun onResume() {
        super.onResume()
        setRecycler()
    }
}