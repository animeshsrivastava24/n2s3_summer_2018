/**
  * Created by omariott on 16/02/17.
  */

package fr.univ_lille.cristal.emeraude.n2s3.dsl

import java.util.NoSuchElementException

import fr.univ_lille.cristal.emeraude.n2s3.core.{NeuronConnection, SynapseBuilder}
import fr.univ_lille.cristal.emeraude.n2s3.features.builder.NeuronGroupRef
import fr.univ_lille.cristal.emeraude.n2s3.features.builder.connection.{ConnectionPolicy, ConnectionTypeBuilder}
import fr.univ_lille.cristal.emeraude.n2s3.features.logging.graph.SynapsesWeightGraphBuilderRef

object N2S3DSLImplicits {

  implicit def stringToNeuronGroupRef(id: String)(implicit network: N2S3SimulationDSL): NeuronGroupRef = {
    network.getNeuronGroupRef(id)
  }

  implicit def stringToNeuronGroup(id: String)(implicit network: N2S3SimulationDSL): NeuronGroupDSL = {
    try {
      network.getNeuronGroupById(id)
    }
    catch {
      case _: NoSuchElementException => basicNeuronGroup(id)
    }
  }

  def inputNeuronGroup(id: String)(implicit network: N2S3SimulationDSL): InputNeuronGroupDSL = new InputNeuronGroupDSL(id)
  def basicNeuronGroup(id: String)(implicit network: N2S3SimulationDSL): BasicNeuronGroupDSL = new BasicNeuronGroupDSL(id)

  implicit def stringToConnectionBuilder(id: String)(implicit network: N2S3SimulationDSL): ConnectionBuilder = new ConnectionBuilder(id, network)

  class ConnectionBuilder(originId: String, network: N2S3SimulationDSL) {
    var connectionStrategy : ConnectionTypeBuilder = _

    var destinationId: String = _
    var connectionPolicy : ConnectionPolicy = _
    var neuronConnection : NeuronConnection = _

    def connectsTo(destinationId: String): ConnectionBuilder = {
      this.destinationId = destinationId
      this
    }

    def using(connectionType: ConnectionTypeBuilder): ConnectionBuilder = {
      this.connectionStrategy = connectionType
      this
    }

    def withSynapse(synapseBuilder : SynapseBuilder): Unit ={
      network.getNeuronGroupRef(this.originId)
          .connectTo(
            network.getNeuronGroupRef(this.destinationId),
            this.connectionStrategy.createConnection(() => synapseBuilder.createSynapse))
    }


    def withPolicy(connectionType: ConnectionPolicy): Unit = {
      this.connectionPolicy = connectionType
    }

    def usingSynapse(synapse: NeuronConnection): Unit = {
      this.neuronConnection = synapse
    }
  }

  def observeConnectionsBetween(originId: String, destinationId: String)(implicit network: N2S3SimulationDSL): SynapsesWeightGraphBuilderRef = {
    network.addSynapsesWeightGraph(originId, destinationId)
    network.toN2S3.addNetworkObserver(new SynapsesWeightGraphBuilderRef(stringToNeuronGroupRef(originId), stringToNeuronGroupRef(destinationId)))
  }

}
