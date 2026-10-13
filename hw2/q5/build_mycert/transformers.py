import torch
from constraintflow.lib.polyexp import PolyExpSparse
from constraintflow.lib.symexp import *
from constraintflow.gbcsr.sparse_tensor import SparseTensor
from constraintflow.lib.llist import Llist
from constraintflow.gbcsr.tensor_ops import *
class mycert:
	def Affine(self, abs_elem, prev, curr, poly_size, curr_size, prev_size, input_size, batch_size):
		cse_var_27 = prev.dot(curr.get_metadata('weight', batch_size), abs_elem.get_poly_size())
		cse_var_26 = curr.get_metadata('bias', batch_size)
		cse_var_76 = binary(cse_var_27.get_const(), cse_var_26, operator.add)
		cse_var_77 = cse_var_27.get_mat(abs_elem)
		cse_var_50 = PolyExpSparse(abs_elem.network, cse_var_77 , cse_var_76)
		cse_var_120 = binary(get_dims(cse_var_77), 1, operator.sub)
		vertices_stop1 = False
		cse_var_12 = SparseTensor([], [], 0, torch.tensor([]), dense_const=0.0, type= type(0.0)).unsqueeze(0).unsqueeze(1).unsqueeze(2).repeat(torch.tensor([batch_size, curr_size, poly_size]))
		cse_var_122 = unary(Llist(abs_elem.network, [1]*(cse_var_120), None, None,torch.nonzero(abs_elem.d['llist']).flatten().tolist()).get_metadata('layer', batch_size), operator.neg)
		cse_var_121 = Llist(abs_elem.network, [1]*(cse_var_120), None, None,torch.nonzero(abs_elem.d['llist']).flatten().tolist())
		cse_var_123 = abs_elem.get_elem('L', cse_var_121)
		cse_var_124 = abs_elem.get_elem('U', cse_var_121)
		cse_var_126 = cse_var_124.get_const()
		cse_var_125 = cse_var_124.get_mat(abs_elem)
		cse_var_128 = cse_var_123.get_const()
		cse_var_127 = cse_var_123.get_mat(abs_elem)
		phi_trav_exp1_1_1 = cse_var_50
		while(True):
			cse_var_28 = phi_trav_exp1_1_1.get_mat(abs_elem)
			vertices1_1_1 = binary(cse_var_28, cse_var_12, operator.ne)
			vertices_stop_default1 = get_default_stop([batch_size, curr_size, poly_size], abs_elem, batch_size, curr_size, poly_size)
			vertices_stop_temp1 = binary(SparseTensor([], [], 0, torch.tensor([]), dense_const=vertices_stop1, type= type(vertices_stop1)).unsqueeze(0).unsqueeze(1).unsqueeze(2).repeat(torch.tensor([batch_size, curr_size, poly_size])), vertices_stop_default1, operator.or_)
			vertices1_1_2 = binary(vertices1_1_1, unary(vertices_stop_temp1, operator.not_), operator.and_)
			if(unary(any(vertices1_1_2), operator.not_)):
				break
			priority_vertices1 = get_max_priority(cse_var_122, vertices1_1_2)
			vertices_final_stop1 = binary(vertices_stop_temp1, repeat(unary(priority_vertices1, operator.not_), torch.tensor([batch_size, curr_size, 1])), operator.or_)
			polyexp_stop1 = filter_trav_exp_stop(phi_trav_exp1_1_1, vertices_final_stop1)
			polyexp_not_stop1 = filter_trav_exp_not_stop(phi_trav_exp1_1_1, vertices_final_stop1)
			cse_var_115 = polyexp_not_stop1.get_mat(abs_elem)
			cse_var_112 = cse_var_115.unsqueeze(3)
			cse_var_107 = clamp(cse_var_115, False, 0)
			cse_var_109 = clamp(cse_var_115, True, 0)
			cse_var_103 = clamp(cse_var_112, False, 0)
			cse_var_105 = clamp(cse_var_112, True, 0)
			cse_var_68 = binary(inner_prod(cse_var_109, cse_var_128.squeeze(1)), inner_prod(cse_var_107, cse_var_126.squeeze(1)), operator.add)
			cse_var_69 = binary(inner_prod(cse_var_105.squeeze(3), cse_var_127.squeeze(1)), inner_prod(cse_var_103.squeeze(3), cse_var_125.squeeze(1)), operator.add)
			cse_var_67 = binary(cse_var_68, polyexp_not_stop1.get_const(), operator.add)
			trav_exp1_4_3 = PolyExpSparse(abs_elem.network, binary(cse_var_69, polyexp_stop1.get_mat(abs_elem), operator.add) , binary(cse_var_67, polyexp_stop1.get_const(), operator.add))
			phi_trav_exp1_1_1 = trav_exp1_4_3
		cse_var_66 = Llist(abs_elem.network, [1]*(cse_var_50.mat.dims-1), None, None,torch.nonzero(abs_elem.d['llist']).flatten().tolist())
		cse_var_65 = cse_var_50.get_mat(abs_elem)
		cse_var_24 = Llist(abs_elem.network, [1]*(phi_trav_exp1_1_1.mat.dims-1), None, None,torch.nonzero(abs_elem.d['llist']).flatten().tolist())
		cse_var_116 = phi_trav_exp1_1_1.get_mat(abs_elem)
		cse_var_99 = clamp(cse_var_65, False, 0)
		cse_var_100 = clamp(cse_var_65, True, 0)
		cse_var_118 = abs_elem.get_elem('l', cse_var_66).squeeze(1)
		cse_var_119 = abs_elem.get_elem('u', cse_var_66).squeeze(1)
		l_new = cf_max(binary(binary(inner_prod(clamp(cse_var_116, True, 0), abs_elem.get_elem('l', cse_var_24).squeeze(1)), inner_prod(clamp(cse_var_116, False, 0), abs_elem.get_elem('u', cse_var_24).squeeze(1)), operator.add), phi_trav_exp1_1_1.get_const(), operator.add), binary(binary(inner_prod(cse_var_100, cse_var_118), inner_prod(cse_var_99, cse_var_119), operator.add), cse_var_76, operator.add))
		vertices_stop2 = False
		phi_trav_exp2_5_1 = cse_var_50
		while(True):
			cse_var_13 = phi_trav_exp2_5_1.get_mat(abs_elem)
			vertices2_5_1 = binary(cse_var_13, cse_var_12, operator.ne)
			vertices_stop_default2 = get_default_stop([batch_size, curr_size, poly_size], abs_elem, batch_size, curr_size, poly_size)
			vertices_stop_temp2 = binary(SparseTensor([], [], 0, torch.tensor([]), dense_const=vertices_stop2, type= type(vertices_stop2)).unsqueeze(0).unsqueeze(1).unsqueeze(2).repeat(torch.tensor([batch_size, curr_size, poly_size])), vertices_stop_default2, operator.or_)
			vertices2_5_2 = binary(vertices2_5_1, unary(vertices_stop_temp2, operator.not_), operator.and_)
			if(unary(any(vertices2_5_2), operator.not_)):
				break
			priority_vertices2 = get_max_priority(cse_var_122, vertices2_5_2)
			vertices_final_stop2 = binary(vertices_stop_temp2, repeat(unary(priority_vertices2, operator.not_), torch.tensor([batch_size, curr_size, 1])), operator.or_)
			polyexp_stop2 = filter_trav_exp_stop(phi_trav_exp2_5_1, vertices_final_stop2)
			polyexp_not_stop2 = filter_trav_exp_not_stop(phi_trav_exp2_5_1, vertices_final_stop2)
			cse_var_98 = polyexp_not_stop2.get_mat(abs_elem)
			cse_var_95 = cse_var_98.unsqueeze(3)
			cse_var_90 = clamp(cse_var_98, False, 0)
			cse_var_92 = clamp(cse_var_98, True, 0)
			cse_var_86 = clamp(cse_var_95, False, 0)
			cse_var_88 = clamp(cse_var_95, True, 0)
			cse_var_57 = binary(inner_prod(cse_var_92, cse_var_126.squeeze(1)), inner_prod(cse_var_90, cse_var_128.squeeze(1)), operator.add)
			cse_var_58 = binary(inner_prod(cse_var_88.squeeze(3), cse_var_125.squeeze(1)), inner_prod(cse_var_86.squeeze(3), cse_var_127.squeeze(1)), operator.add)
			cse_var_56 = binary(cse_var_57, polyexp_not_stop2.get_const(), operator.add)
			trav_exp2_8_3 = PolyExpSparse(abs_elem.network, binary(cse_var_58, polyexp_stop2.get_mat(abs_elem), operator.add) , binary(cse_var_56, polyexp_stop2.get_const(), operator.add))
			phi_trav_exp2_5_1 = trav_exp2_8_3
		cse_var_10 = Llist(abs_elem.network, [1]*(phi_trav_exp2_5_1.mat.dims-1), None, None,torch.nonzero(abs_elem.d['llist']).flatten().tolist())
		cse_var_101 = phi_trav_exp2_5_1.get_mat(abs_elem)
		u_new = cf_min(binary(binary(inner_prod(clamp(cse_var_101, True, 0), abs_elem.get_elem('u', cse_var_10).squeeze(1)), inner_prod(clamp(cse_var_101, False, 0), abs_elem.get_elem('l', cse_var_10).squeeze(1)), operator.add), phi_trav_exp2_5_1.get_const(), operator.add), binary(binary(inner_prod(cse_var_100, cse_var_119), inner_prod(cse_var_99, cse_var_118), operator.add), cse_var_76, operator.add))
		return l_new, u_new, cse_var_50, cse_var_50
	
	def Relu(self, abs_elem, prev, curr, poly_size, curr_size, prev_size, input_size, batch_size):
		cse_var_47 = abs_elem.get_elem('l', prev)
		cse_var_48 = SparseTensor([], [], 0, torch.tensor([]), dense_const=0.0, type= type(0.0)).unsqueeze(0).unsqueeze(1).repeat(torch.tensor([batch_size, curr_size]))
		cse_var_55 = binary(cse_var_47, cse_var_48, operator.ge)
		rewrite_new_0 = convert_to_float(cse_var_55)
		cse_var_117 = SparseTensor([], [], 0, torch.tensor([]), dense_const=1.0, type= type(1.0)).unsqueeze(0).unsqueeze(1).repeat(torch.tensor([batch_size, curr_size]))
		l_new = binary(binary(rewrite_new_0, cse_var_47, operator.mul), binary(binary(cse_var_117, rewrite_new_0, operator.sub), cse_var_48, operator.mul), operator.add)
		cse_var_45 = abs_elem.get_elem('u', prev)
		rewrite_new_1 = convert_to_float(binary(cse_var_45, cse_var_48, operator.ge))
		u_new = binary(binary(rewrite_new_1, cse_var_45, operator.mul), binary(binary(cse_var_117, rewrite_new_1, operator.sub), cse_var_48, operator.mul), operator.add)
		cse_var_46 = prev.convert_to_poly(abs_elem)
		cse_var_53 = repeat(cse_var_46.get_const(), torch.tensor([batch_size, 1]))
		cse_var_42 = PolyExpSparse(abs_elem.network, 0.0, cse_var_48)
		cse_var_32 = cse_var_42.get_const()
		cse_var_33 = binary(cse_var_45, cse_var_47, operator.sub)
		cse_var_34 = cse_var_42.get_mat(abs_elem)
		cse_var_43 = binary(cse_var_45, cse_var_48, operator.le)
		cse_var_35 = repeat(cse_var_43.unsqueeze(2), torch.tensor([1, 1, poly_size]))
		cse_var_54 = repeat(cse_var_46.get_mat(abs_elem), torch.tensor([batch_size, 1, 1]))
		cse_var_37 = repeat(cse_var_55.unsqueeze(2), torch.tensor([1, 1, poly_size]))
		cse_var_44 = binary(cse_var_45, cse_var_33, operator.truediv)
		cse_var_38 = repeat(cse_var_44.unsqueeze(2), torch.tensor([1, 1, poly_size]))
		cse_var_83 = binary(cse_var_44, cse_var_53, operator.mul)
		cse_var_84 = binary(cse_var_38, cse_var_54, operator.mul)
		cse_var_81 = where(cse_var_43, cse_var_32, cse_var_83)
		cse_var_82 = where(cse_var_35, cse_var_34, cse_var_84)
		cse_var_79 = where(cse_var_37, cse_var_54, cse_var_82)
		L_new = PolyExpSparse(abs_elem.network, cse_var_79 , where(cse_var_55, cse_var_53, cse_var_81))
		cse_var_80 = binary(cse_var_83, binary(binary(cse_var_45, cse_var_47, operator.mul), cse_var_33, operator.truediv), operator.sub)
		cse_var_78 = where(cse_var_43, cse_var_32, cse_var_80)
		U_new = PolyExpSparse(abs_elem.network, cse_var_79 , where(cse_var_55, cse_var_53, cse_var_78))
		return l_new, u_new, L_new, U_new
	
